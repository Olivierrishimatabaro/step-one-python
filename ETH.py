# ethereum_org_contributor.py
# A helper script to guide contributors to ethereum.org

def welcome_message():
    print("Welcome to ethereum.org!")
    print("This repo is a resource for the Ethereum community.")
    print("Purpose: 'Be the best portal to Ethereum for our growing global community'\n")

def looking_for_blockchain_code():
    print("Looking for Ethereum blockchain code?")
    print("Ethereum has multiple protocol implementations in different languages.\n")

def table_of_contents():
    print("Table of Contents:")
    print("1. How to contribute")
    print("2. Translation Program")
    print("3. Website stack")
    print("4. Conventions / best practices\n")

def contribution_steps():
    print("Contribution Steps:")
    
    # Step 1
    print("\nStep 1: Submit an Issue")
    print(" - Create a new issue on GitHub")
    print(" - Comment if you want to be assigned")
    
    # Step 2
    print("\nStep 2: Fork the repository")
    print(" - Fork it via GitHub interface")
    
    # Step 3
    print("\nStep 3: Set up local environment")
    print("Clone your fork:")
    print("git clone git@github.com:[your_github_handle]/ethereum-org-website.git")
    print("cd ethereum-org-website")
    print("Configure fork:")
    print("git remote add upstream https://github.com/ethereum/ethereum-org-website.git")
    print("git checkout dev")
    print("git fetch upstream")
    print("git merge upstream/dev")
    print("Use Node.js version via nvm:")
    print("nvm use")
    print("Enable Corepack:")
    print("corepack enable")
    print("Install dependencies:")
    print("pnpm install\n")

    # Step 4
    print("Step 4: Make changes!")
    print("Create a new branch: git checkout -b new_branch_name")
    print("Start development: pnpm dev")
    print("Commit changes: git commit -m 'brief description [Fixes #1234]'")
    print("Push to GitHub: git push\n")

    # Step 5
    print("Step 5: Submit PR")
    print(" - Submit a PR to dev branch")
    print(" - Reference the issue in PR description")
    print(" - Netlify deploy preview available automatically\n")

    # Step 6 & 7
    print("Step 6: Wait for review")
    print("Step 7: Release - master branch auto-deploys to Netlify\n")

def poap_oat_info():
    print("POAP & OATs Info:")
    print(" - POAP: Proof of Attendance Protocol badge (ERC-721 token)")
    print(" - GitPOAP: Merged contributions earn a contributor POAP")
    print(" - OAT: Onchain Achievement Token on Galxe")
    print(" - Claim your OATs via Discord #🥇 | proof-of-contribution\n")

def main():
    welcome_message()
    looking_for_blockchain_code()
    table_of_contents()
    contribution_steps()
    poap_oat_info()
    print("Start contributing today to earn POAP/OATs and support the Ethereum community!")

if __name__ == "__main__":
    main()
