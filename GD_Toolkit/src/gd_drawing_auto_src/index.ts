import { renderFunctions } from "./render_fcts.js";
import type { RenderOptions } from "./render_fcts.js";

export async function generateDocumentationImages(
    options: RenderOptions
): Promise<void> {

    const result = await renderFunctions(options);

    if (result.stdout) {
        console.log(result.stdout.trimEnd());
    }

    if (result.stderr) {
        console.error(result.stderr.trimEnd());
    }
}