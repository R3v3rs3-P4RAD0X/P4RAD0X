use std::{process::Command, io::Write};
use strum::IntoEnumIterator;
use strum_macros::{EnumIter, Display};

// Constants
const BASE_PATH: &str = "/P4RAD0X/projects";

#[derive(EnumIter, Display)]
enum Language {
    Rust,
    Python,
    Cpp,
    JavaScript,
    Ruby,
    Go,
    Bash,
    Web
}

impl Language {
    fn to_string(&self) -> String {
        match self {
            Language::Rust => "rust".to_string(),
            Language::Python => "python".to_string(),
            Language::Cpp => "cpp".to_string(),
            Language::JavaScript => "javascript".to_string(),
            Language::Ruby => "ruby".to_string(),
            Language::Go => "go".to_string(),
            Language::Bash => "bash".to_string(),
            Language::Web => "web".to_string(),
        }
    }

    fn from_string(language: String) -> Language {
        match language.to_lowercase().as_str() {
            "rust" => Language::Rust,
            "python" => Language::Python,
            "py" => Language::Python,
            "cpp" => Language::Cpp,
            "c++" => Language::Cpp,
            "javascript" => Language::JavaScript,
            "js" => Language::JavaScript,
            "ruby" => Language::Ruby,
            "go" => Language::Go,
            "bash" => Language::Bash,
            "web" => Language::Web,
            "www" => Language::Web,
            _ => panic!("Invalid language"),
        }
    }
}


struct Project {
    name: String,
    description: String,
    language: Language,
}

impl Project {
    fn new(name: String, description: String, language: Language) -> Project {
        Project {
            name,
            description,
            language,
        }
    }

    fn create_path(&self) -> String {
        format!("{}/{}/{}", BASE_PATH, self.language.to_string(), self.name)
    }

    fn create_readme(&self) {
        // Create the path
        let path = self.create_path();

        // Create the readme
        Command::new("touch")
            .arg(format!("{}/README.md", path))
            .status()
            .unwrap();

        // Open the readme to write into
        let mut readme = std::fs::OpenOptions::new()
            .write(true)
            .open(format!("{}/README.md", path))
            .unwrap();

        // Split the name by - or _ or spaces
        let name_split = self.name.split(|c| c == '-' || c == '_' || c == ' ');

        // Convert the name to title case
        let mut title_case = String::new();
        for word in name_split {
            title_case.push_str(&to_title_case(word));
            
            // Check if the word is not the last word
            if word != self.name.split(|c| c == '-' || c == '_' || c == ' ').last().unwrap() {
                title_case.push_str(" ");
            }
        }

        // Write the title
        readme
            .write_all(format!("# {}\n\n", title_case).as_bytes())
            .unwrap();

        // Write the description
        readme
            .write_all(format!("{}\n", self.description).as_bytes())
            .unwrap();

        // Close the readme
        readme.flush().unwrap();
    }

    fn save(&self) {
        // Create a new file in /P4RAD0X/project-alpha/projects.yml
        let mut projects = std::fs::OpenOptions::new()
            .write(true)
            .append(true)
            .open("/P4RAD0X/project-alpha/projects.yml")
            .expect("Failed to open projects.yml");

        // Write the project
        // In the format:
        // - <name>:
        //     description: <description>
        //     language: <language>
        projects
            .write_all(format!("\n\t- {}: \n", self.name).as_bytes())
            .unwrap();

        projects
            .write_all(format!("\t\tdescription: {}\n", self.description).as_bytes())
            .unwrap();

        projects
            .write_all(format!("\t\tlanguage: {}\n", self.language.to_string()).as_bytes())
            .unwrap();

        // Write a new line
        projects.write_all(b"\n").unwrap();

        // Close the file
        projects.flush().unwrap();
    }

    fn create_directory(&self) -> String {
        // Create the path
        let path = self.create_path();

        // Create a new directory
        Command::new("mkdir")
            .arg("-p")
            .arg(&path)
            .status()
            .unwrap();

        // Return the path
        path
    }

    fn setup(&self) {
        match self.language {
            Language::Rust => {
                // Create the path
                let path = self.create_path();

                // Create a new cargo project
                Command::new("cargo")
                    .arg("new")
                    .arg(&path)
                    .status()
                    .unwrap();

                // Create the readme
                self.create_readme();
            }
            Language::Python => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.py", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.py", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"def main():\n").unwrap();
                main.write_all(b"    pass\n").unwrap();
                main.write_all(b"\n").unwrap();

                // Write the main function
                main.write_all(b"if __name__ == \"__main__\":\n").unwrap();
                main.write_all(b"    main()\n").unwrap();

                // Close the main file
                main.flush().unwrap();

                // Create a virtual environment
                Command::new("python")
                    .arg("-m")
                    .arg("venv")
                    .arg(format!("{}/.env", path))
                    .status()
                    .unwrap();

                // Create a requirements file
                Command::new("touch")
                    .arg(format!("{}/requirements.txt", path))
                    .status()
                    .unwrap();
            }
            Language::Cpp => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.cpp", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.cpp", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"#include <iostream>\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"int main() {\n").unwrap();
                main.write_all(b"    return 0;\n").unwrap();
                main.write_all(b"}\n").unwrap();

                // Close the main file
                main.flush().unwrap();

                // Create a makefile
                Command::new("touch")
                    .arg(format!("{}/Makefile", path))
                    .status()
                    .unwrap();

                // Open the makefile to write into
                let mut makefile = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/Makefile", path))
                    .unwrap();

                // Write the makefile
                makefile.write_all(b"CC=g++\n").unwrap();
                makefile.write_all(b"CFLAGS=-Wall -Wextra -pedantic -std=c++17\n").unwrap();
                makefile.write_all(b"\n").unwrap();
                makefile.write_all(b"all: main\n").unwrap();
                makefile.write_all(b"\n").unwrap();
                makefile.write_all(b"main: main.cpp\n").unwrap();
                makefile.write_all(b"    $(CC) $(CFLAGS) -o main main.cpp\n").unwrap();
                makefile.write_all(b"\n").unwrap();
                makefile.write_all(b"clean:\n").unwrap();
                makefile.write_all(b"    rm -f main\n").unwrap();

                // Close the makefile
                makefile.flush().unwrap();

                // Create a gitignore
                Command::new("touch")
                    .arg(format!("{}/.gitignore", path))
                    .status()
                    .unwrap();

                // Open the gitignore to write into
                let mut gitignore = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/.gitignore", path))
                    .unwrap();

                // Write the gitignore
                gitignore.write_all(b"main\n").unwrap();

                // Close the gitignore
                gitignore.flush().unwrap();
            }
            Language::JavaScript => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.js", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.js", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"function main() {\n").unwrap();
                main.write_all(b"    return 0;\n").unwrap();
                main.write_all(b"}\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"if (require.main === module) {\n").unwrap();
                main.write_all(b"    main();\n").unwrap();
                main.write_all(b"}\n").unwrap();

                // Close the main file
                main.flush().unwrap();
            }
            Language::Ruby => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.rb", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.rb", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"def main\n").unwrap();
                main.write_all(b"    return 0\n").unwrap();
                main.write_all(b"end\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"if __FILE__ == $0\n").unwrap();
                main.write_all(b"    main\n").unwrap();
                main.write_all(b"end\n").unwrap();

                // Close the main file
                main.flush().unwrap();
            }
            Language::Go => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.go", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.go", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"package main\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"func main() {\n").unwrap();
                main.write_all(b"    return 0\n").unwrap();
                main.write_all(b"}\n").unwrap();

                // Close the main file
                main.flush().unwrap();
            }
            Language::Bash => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/main.sh", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/main.sh", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"#!/bin/bash\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"main() {\n").unwrap();
                main.write_all(b"    return 0\n").unwrap();
                main.write_all(b"}\n").unwrap();

                // Close the main file
                main.flush().unwrap();
            }
            Language::Web => {
                // Create the directory
                let path = self.create_directory();

                // Create the readme
                self.create_readme();

                // Create the main file
                Command::new("touch")
                    .arg(format!("{}/index.html", path))
                    .status()
                    .unwrap();

                // Open the main file to write into
                let mut main = std::fs::OpenOptions::new()
                    .write(true)
                    .open(format!("{}/index.html", path))
                    .unwrap();

                // Write the main file
                main.write_all(b"<!DOCTYPE html>\n").unwrap();
                main.write_all(b"<html>\n").unwrap();
                main.write_all(b"<head>\n").unwrap();
                main.write_all(b"    <title></title>\n").unwrap();
                main.write_all(b"    <link rel=\"stylesheet\" href=\"styles/main.css\">\n").unwrap();
                main.write_all(b"</head>\n").unwrap();
                main.write_all(b"<body>\n").unwrap();
                main.write_all(b"\n").unwrap();
                main.write_all(b"    <script src=\"src/main.js\"></script>\n").unwrap();
                main.write_all(b"</body>\n").unwrap();
                main.write_all(b"</html>\n").unwrap();

                // Close the main file
                main.flush().unwrap();

                // Create the src and styles directories
                Command::new("mkdir")
                    .arg("-p")
                    .arg(format!("{}/src", path))
                    .status()
                    .unwrap();

                Command::new("mkdir")
                    .arg("-p")
                    .arg(format!("{}/styles", path))
                    .status()
                    .unwrap();

                // Create the main.js file
                Command::new("touch")
                    .arg(format!("{}/src/main.js", path))
                    .status()
                    .unwrap();

                // Create the main.css file
                Command::new("touch")
                    .arg(format!("{}/styles/main.css", path))
                    .status()
                    .unwrap();
            }
        }
    
    }
}

fn to_title_case(string: &str) -> String {
    // Convert the first character to uppercase
    let mut title_case = string.chars().next().unwrap().to_uppercase().to_string();

    // Convert the rest of the characters to lowercase
    for character in string.chars().skip(1) {
        title_case.push_str(&character.to_lowercase().to_string());
    }

    // Return the title case
    title_case
}

fn ask(question: &str) -> String {
    println!("{}", question);
    let mut answer = String::new();
    std::io::stdin().read_line(&mut answer).unwrap();
    answer.trim().to_string()
}

fn main() {
    // Clear the screen
    Command::new("clear").status().unwrap();

    // Print the welcome message
    println!("Welcome to Project Alpha!");
    println!("-------------------------");

    // Get the project name
    let name = ask("What is the name of your project?");

    // Get the project description
    let description = ask("What is the description of your project?");

    // Create a variable for the language
    let language: Language;
    
    // Print all the languages
    println!("Languages:");
    for language in Language::iter() {
        println!("  - {}", language.to_string());
    }

    loop {
        let language_string = ask("What is the language of your project?");
        match Language::from_string(language_string) {
            Language::Rust => {
                language = Language::Rust;
                break;
            }
            Language::Python => {
                language = Language::Python;
                break;
            }
            Language::Cpp => {
                language = Language::Cpp;
                break;
            }
            Language::JavaScript => {
                language = Language::JavaScript;
                break;
            }
            Language::Ruby => {
                language = Language::Ruby;
                break;
            }
            Language::Go => {
                language = Language::Go;
                break;
            }
            Language::Bash => {
                language = Language::Bash;
                break;
            }
            Language::Web => {
                language = Language::Web;
                break;
            }
        }
        
    }

    // Create the project
    let project = Project::new(name, description, language);

    // Setup the project
    project.setup();

    // Save the project
    project.save();
}
