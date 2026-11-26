import { defineConfig,  globalIgnores } from "eslint/config";


export default defineConfig([
    globalIgnores([
        "GeometricalDomination/**",
        "TurtleExtension/**",
        "UniversalFunctions/**",
        ".vscode/**"
    ])
])