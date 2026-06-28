import argparse
import os
import sys

def check_self_plagiarism(draft_path, ref_dir):
    try:
        with open(draft_path, 'r', encoding='utf-8') as f:
            draft_text = f.read()
    except Exception as e:
        print(f"Error reading draft: {e}")
        sys.exit(1)

    print(f"Checking '{draft_path}' against references in '{ref_dir}'...")
    
    found_issue = False
    for root, _, files in os.walk(ref_dir):
        for file in files:
            if file.endswith('.txt') or file.endswith('.tex'):
                ref_path = os.path.join(root, file)
                try:
                    with open(ref_path, 'r', encoding='utf-8') as f:
                        ref_text = f.read()
                        
                    # Very crude chunk-based overlap check
                    chunk_size = 200
                    draft_chunks = [draft_text[i:i+chunk_size] for i in range(0, len(draft_text), chunk_size)]
                    for chunk in draft_chunks:
                        if len(chunk) < 50:
                            continue
                        if chunk in ref_text:
                            print(f"⚠️ High overlap found with {file}! Segment: '{chunk[:50]}...'")
                            found_issue = True
                            
                except Exception as e:
                    print(f"Skipping {file}: {e}")

    if not found_issue:
        print("✅ No exact large block overlaps found with reference documents.")

def main():
    parser = argparse.ArgumentParser(description="Self-plagiarism basic checker")
    parser.add_argument("draft", type=str, help="Path to the current draft (.txt or .tex)")
    parser.add_argument("ref_dir", type=str, help="Directory containing past papers (.txt or .tex)")
    args = parser.parse_args()

    if not os.path.isdir(args.ref_dir):
        print(f"Reference directory not found: {args.ref_dir}")
        sys.exit(1)

    check_self_plagiarism(args.draft, args.ref_dir)

if __name__ == "__main__":
    main()
