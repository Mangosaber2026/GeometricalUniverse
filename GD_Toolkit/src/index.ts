import * as gd_check from "#gd-verification/index";
import * as ts_uf from "#ts-utilities/index";
import * as fileEdit from "#file-editing/index";

async function CheckGD(): Promise<void> {
    ts_uf.ConsoleToolkit.information("GD_Toolkit started!");

    const compatible = await gd_check.checkPython();

    if (!compatible) {
        ts_uf.ConsoleToolkit.error("GD environment check failed!");
        return;
    };

    await gd_check.getInfoGD();

    ts_uf.ConsoleToolkit.success("GD environment check passed!");
};

async function getIndexHTMLContent(): Promise<string> {
    const file_path: string = await fileEdit.readFile("../GeometricalDomination/gd/visuals/premade_shapes/premade_shapes_docs/shapes.md");

    console.log(file_path);

    return file_path
};

function CreateABCMarkdown(): string {
    let total_markdown: string = "";

    for (const letter of ts_uf.asciiUpperCase) {
        total_markdown += `
#### ${letter}

##### Preview: ${letter}

![letter ${letter} showcase](./images/letter_${letter}_showcase.png)

[letter ${letter} showcase](./images/letter_${letter}_showcase.png)

##### Source code: ${letter}

[Click here to inspect the source code of EngLetters.${letter}()](https://github.com/Mangosaber2026/GeometricalDomination/blob/main/gd/visuals/eng_alphabets/english_letters.py)

Comment Linking: [[#EngLetters-${letter}-anchor|EngLetters_${letter}()]] 
`;
    };

    return total_markdown
}

import {
    generateDocumentationImages
} from "./gd_drawing_auto_src/index.js";

async function main(): Promise<void> {

    await generateDocumentationImages({
        toolkitRoot: "." /* your discovered GD_Toolkit root */,
        pythonWorkingDirectory:  /* Python import working directory */,
        pythonImportRoot:  /* directory containing the importable GD package */,
        functions: [
            "EngAlphabets.A",
            "EngAlphabets.B",
            "EngAlphabets.C"
        ],
        height: 200,
        color: "blue",
        outputDirectory: /* absolute images directory */
    });

}

main().catch(error => {
    console.error(error);
    process.exitCode = 1;
});