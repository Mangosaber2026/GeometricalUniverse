
interface Project {
    name: string;
    description: string;
    color: string;
}

function ProjectCard({ name, description, color }: Project) {
    return (
        <article style={{ borderColor: color }}>
            <h2 style={{ color }}>{name}</h2>
            <p>{description}</p>
        </article>
    );
}

function App() {
    console.log("GeometricalUniverse loaded!");

    const projects: Project[] = [
        {
            name: "GeometricalDomination",
            description: "Python geometric drawings.",
            color: "#70b7ff"
        },
        {
            name: "GD_Toolkit",
            description: "Development utilities.",
            color: "#a78bfa"
        },
        {
            name: "ShapesMultiverse",
            description: "Mathematical visualisations.",
            color: "#34d399"
        }
    ];

    return (
        <main>
            <h1>GeometricalUniverse</h1>

            {projects.map(project => (
                <ProjectCard
                    key={project.name}
                    {...project}
                />
            ))}
        </main>
    );
}

export default App;
