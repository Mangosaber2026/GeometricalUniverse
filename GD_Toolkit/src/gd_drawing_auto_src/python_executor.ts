import { spawn } from "node:child_process";

export interface PythonLaunch {
    executable: string;
    args: string[];
}

export interface PythonExecution {
    launch: PythonLaunch;
    scriptPath: string;
    cwd: string;
    input: unknown;
}

export interface PythonResult {
    stdout: string;
    stderr: string;
}

export function executePython({
    launch,
    scriptPath,
    cwd,
    input
}: PythonExecution): Promise<PythonResult> {

    return new Promise((resolve, reject) => {

        const child = spawn(
            launch.executable,
            [...launch.args, scriptPath],
            {
                cwd,
                stdio: ["pipe", "pipe", "pipe"]
            }
        );

        let stdout = "";
        let stderr = "";

        child.stdout.setEncoding("utf8");
        child.stderr.setEncoding("utf8");

        child.stdout.on("data", (data: string) => {
            stdout += data;
        });

        child.stderr.on("data", (data: string) => {
            stderr += data;
        });

        child.once("error", reject);

        child.once("close", (code, signal) => {

            if (code === 0) {
                resolve({ stdout, stderr });
                return;
            }

            reject(
                new Error(
                    [
                        "Python execution failed.",
                        `Exit code: ${code}`,
                        `Signal: ${signal}`,
                        `STDOUT: ${stdout}`,
                        `STDERR: ${stderr}`
                    ].join("\n")
                )
            );
        });

        child.stdin.end(JSON.stringify(input));
    });
}