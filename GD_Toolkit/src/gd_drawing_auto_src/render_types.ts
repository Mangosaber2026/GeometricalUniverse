export interface GeneratedImage {
    function: string;
    output: string;
    status: "success" | "failiure";
}

export interface RenderReport {
    generated: GeneratedImage[];
    failed: GeneratedImage[];
    total: number;
}
