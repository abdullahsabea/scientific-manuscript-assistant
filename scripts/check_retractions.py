import argparse
import urllib.request
import urllib.error
import json
import re
import sys

def check_doi_crossref(doi):
    url = f"https://api.crossref.org/works/{doi}"
    req = urllib.request.Request(url, headers={'User-Agent': 'ScientificManuscriptAssistant/1.0 (mailto:admin@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                message = data.get('message', {})
                update_policy = message.get('update-policy', None)
                is_retracted = False
                
                # Crossref sometimes includes 'update-to' indicating retraction or correction
                updates = message.get('update-to', [])
                for update in updates:
                    if update.get('type') == 'retraction':
                        is_retracted = True
                        break
                
                if is_retracted:
                    return "🚨 RETRACTED"
                elif update_policy:
                    return "⚠️ HAS UPDATES/CORRECTIONS (Check manually)"
                else:
                    return "✅ OK (No known retractions in Crossref)"
            else:
                return f"❓ API ERROR ({response.status})"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "❓ DOI NOT FOUND in Crossref"
        else:
            return f"❓ API ERROR ({e.code})"
    except Exception as e:
        return f"❓ REQUEST ERROR: {e}"

def extract_dois_from_bib(bib_content):
    # Simple regex to find doi={...}
    dois = re.findall(r'doi\s*=\s*[{"](10\.\d{4,9}/[-._;()/:A-Z0-9]+)[}"]', bib_content, flags=re.IGNORECASE)
    return dois

def main():
    parser = argparse.ArgumentParser(description="Check DOIs against Crossref API for retraction/update notices.")
    parser.add_argument('--doi', type=str, help="A single DOI to check")
    parser.add_argument('--bib', type=str, help="Path to a .bib file to scan for DOIs")
    args = parser.parse_args()

    dois_to_check = []

    if args.doi:
        dois_to_check.append(args.doi)
    
    if args.bib:
        try:
            with open(args.bib, 'r', encoding='utf-8') as f:
                content = f.read()
                dois = extract_dois_from_bib(content)
                dois_to_check.extend(dois)
        except Exception as e:
            print(f"Error reading {args.bib}: {e}")
            sys.exit(1)

    if not dois_to_check:
        print("No DOIs provided or found.")
        sys.exit(1)

    dois_to_check = list(set(dois_to_check)) # remove duplicates
    print(f"Checking {len(dois_to_check)} unique DOIs...")
    
    for doi in dois_to_check:
        status = check_doi_crossref(doi)
        print(f"[{status}] {doi}")

if __name__ == "__main__":
    main()
