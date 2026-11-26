import { resolve } from "node:path";
import {
    executePython,
    type PythonResult
} from "./python_executor.js";

export interface RenderOptions {
    toolkitRoot: string;
    pythonWorkingDirectory: string;
    pythonImportRoot: string;
    functions: string[];
    height: number;
    color: string;
    outputDirectory: string;
}

export async function renderFunctions(
    options: RenderOptions
): Promise<PythonResult> {

    const rendererPath = resolve(
        options.toolkitRoot,
        "publishing_src",
        "documentation_generation",
        "python",
        "turtle_renderer.py"
    );

    const isWindows = process.platform === "win32";

    return executePython({
        launch: {
            executable: isWindows ? "py" : "python3",
            args: isWindows ? ["-3.15"] : []
        },

        scriptPath: rendererPath,

        cwd: options.pythonWorkingDirectory,

        input: {
            pythonImportRoot: options.pythonImportRoot,
            functions: options.functions,
            height: options.height,
            color: options.color,
            outputDirectory: options.outputDirectory
        }
    });
}