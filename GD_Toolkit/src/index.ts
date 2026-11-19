import * as gd_check from "#gd-verification/index";
import * as ts_uf from "#ts-utilities/index";
import * as fileEdit from "#file-editing/index";

async function main(): Promise<void> {
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

await main()