import os
import json
import argparse

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def init_typescript(args):
    # package.json
    package_json = {
        "name": args.name,
        "version": "0.0.0",
        "description": args.description,
        "main": "dist/index.js",
        "scripts": {
            "bundle": "ncc build src/index.ts --source-map --license licenses.txt",
            "test": "jest",
            "lint": "eslint src/**/*.ts",
            "format": "prettier --write src/**/*.ts",
            "all": "npm run format && npm run lint && npm run test && npm run bundle"
        },
        "dependencies": {
            "@actions/core": "^1.11.1",
            "@actions/github": "^6.0.1"
        },
        "devDependencies": {
            "@types/jest": "^29.5.14",
            "@types/node": "^22.10.2",
            "@vercel/ncc": "^0.38.3",
            "jest": "^29.7.0",
            "ts-jest": "^29.2.5",
            "typescript": "^5.7.2"
        }
    }
    create_file(os.path.join(args.path, 'package.json'), json.dumps(package_json, indent=2))

    # action.yml
    action_yml = f"""
name: '{args.name}'
description: '{args.description}'
author: 'GitHub Actions Creator Skill'
branding:
  icon: '{args.icon}'
  color: '{args.color}'
inputs:
  milliseconds:
    description: 'Example input'
    required: false
    default: '1000'
outputs:
  time:
    description: 'The time the action finished'
runs:
  using: 'node20'
  main: 'dist/index.js'
"""
    create_file(os.path.join(args.path, 'action.yml'), action_yml)

    # tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "ES2022",
            "module": "NodeNext",
            "moduleResolution": "NodeNext",
            "outDir": "dist",
            "rootDir": "src",
            "strict": True,
            "esModuleInterop": True,
            "skipLibCheck": True,
            "forceConsistentCasingInFileNames": True
        }
    }
    create_file(os.path.join(args.path, 'tsconfig.json'), json.dumps(tsconfig, indent=2))

    # src/main.ts
    main_ts = """
import * as core from '@actions/core'

/**
 * The main function for the action.
 * @returns {Promise<void>} Resolves when the action is complete.
 */
export async function run(): Promise<void> {
  try {
    const ms: string = core.getInput('milliseconds')

    // Debug logs are only output if the 1G_SECRET_DEBUG is set
    core.debug(`Waiting ${ms} milliseconds ...`)

    // Log the current time
    core.info(new Date().toTimeString())

    // Set outputs for other workflow steps to use
    core.setOutput('time', new Date().toTimeString())
  } catch (error) {
    // Fail the workflow run if an error occurs
    if (error instanceof Error) core.setFailed(error.message)
  }
}
"""
    create_file(os.path.join(args.path, 'src/main.ts'), main_ts)

    # src/index.ts
    index_ts = """
import { run } from './main.js'

// eslint-disable-next-line @typescript-eslint/no-floating-promises
run()
"""
    create_file(os.path.join(args.path, 'src/index.ts'), index_ts)

def init_composite(args):
    action_yml = f"""
name: '{args.name}'
description: '{args.description}'
author: 'GitHub Actions Creator Skill'
branding:
  icon: '{args.icon}'
  color: '{args.color}'
inputs:
  who-to-greet:
    description: 'Who to greet'
    required: true
    default: 'World'
outputs:
  random-number:
    description: "Random number"
    value: ${{{{ steps.random-number-generator.outputs.random-number }}}}
runs:
  using: "composite"
  steps:
    - run: echo Hello ${{{{ inputs.who-to-greet }}}}
      shell: bash
    - id: random-number-generator
      run: echo "random-number=$(echo $RANDOM)" >> $GITHUB_OUTPUT
      shell: bash
"""
    create_file(os.path.join(args.path, 'action.yml'), action_yml)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    parser.add_argument('--description', default='')
    parser.add_argument('--path', required=True)
    parser.add_argument('--type', choices=['typescript', 'composite'], default='typescript')
    parser.add_argument('--icon', default='activity')
    parser.add_argument('--color', default='blue')
    args = parser.parse_args()

    if args.type == 'typescript':
        init_typescript(args)
    else:
        init_composite(args)

    # Common README.md
    readme = f"""
# {args.name}

{args.description}

## Usage

```yaml
- uses: actions/checkout@v4
- uses: ./{os.path.relpath(args.path, '.')} 
  with:
    # inputs go here
```
"""
    create_file(os.path.join(args.path, 'README.md'), readme)

    # Test workflow
    test_workflow = f"""
name: Test Action
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Test local action
        uses: ./
        with:
          # Add inputs if needed
"""
    create_file(os.path.join(args.path, '.github/workflows/test-action.yml'), test_workflow)

if __name__ == "__main__":
    main()
