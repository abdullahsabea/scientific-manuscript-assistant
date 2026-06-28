import argparse
import re
import sys

def check_latex(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    
    # Check unbalanced braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        errors.append(f"Unbalanced braces: {open_braces} open '{{', {close_braces} close '}}'.")

    # Check unclosed environments
    begin_envs = re.findall(r'\\begin\{([^}]+)\}', content)
    end_envs = re.findall(r'\\end\{([^}]+)\}', content)
    
    env_counts = {}
    for env in begin_envs:
        env_counts[env] = env_counts.get(env, 0) + 1
    for env in end_envs:
        env_counts[env] = env_counts.get(env, 0) - 1
        
    for env, count in env_counts.items():
        if count > 0:
            errors.append(f"Unclosed environment: \\begin{{{env}}} is missing a corresponding \\end{{{env}}}.")
        elif count < 0:
            errors.append(f"Dangling environment: \\end{{{env}}} is missing a corresponding \\begin{{{env}}}.")

    # Basic check for empty cite or ref
    if re.search(r'\\cite\{\s*\}', content):
        errors.append("Empty \\cite{} command found.")
    if re.search(r'\\ref\{\s*\}', content):
        errors.append("Empty \\ref{} command found.")

    if not errors:
        print("✅ LaTeX syntax looks okay (Basic verification passed).")
        return True
    else:
        print("❌ LaTeX syntax issues found:")
        for err in errors:
            print(f"  - {err}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Basic LaTeX syntax validator.")
    parser.add_argument("file", type=str, help="Path to the .tex file to check")
    args = parser.parse_args()
    
    try:
        check_latex(args.file)
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        sys.exit(1)

if __name__ == "__main__":
    main()
