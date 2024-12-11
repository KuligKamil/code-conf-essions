# "scripts": {

from yaml import safe_load


def main() -> None:
    try:
        project_name, content = "", ""
        with open(".copier-answers.yml") as f:
            content = safe_load(f.read())
            project_name = content["project_name"]
        with open("package.json", "r") as f:
            content = f.read()
            content = content.replace(
                '  "scripts": {',
                '  "scripts": { \n'
                + f'    "{project_name}": "slidev --open {project_name}/main.md",\n    "export-{project_name}": "slidev export {project_name}/main.md -output prod/{project_name}",',
            )
        with open("package.json", "w") as f:
            f.write(content)
    except Exception as e:
        print(e)


# "export-ps2024": "slidev export p-s-2024/main.md",
# if __name__ == "__main__":
main()
