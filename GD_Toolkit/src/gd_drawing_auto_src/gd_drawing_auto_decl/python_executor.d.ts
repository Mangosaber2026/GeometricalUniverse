/**
 * Declares interface for the arguments required for the Python launch process.
 */
export declare interface PythonLaunch {
    executable: string;
    args: string[];
}


/**
 * Declares interface for the arguments required for the Python execution process.
 */
export declare interface PythonExecution {
    launch: PythonLaunch;
    scriptPath: string;
    cwd: string;
    input: unknown;
}


/**
 * Takes the launch arguments, the script execution directory and others to create the arguments required
 * for the actual Python execution.
 * 
 * @param param0 - Dictionary containing crucial information to execute the Python file which draws 
 * the provided drawing functions from gd.
 */
export declare function executePython({
    launch,
    scriptPath,
    cwd,
    input
}: PythonExecution): Promise<string>;