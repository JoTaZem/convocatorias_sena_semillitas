import { useEffect, useState } from "react";

function ListarConvocatorias() {
    const [convocatorias, setConvocatorias] = useState([]);

    useEffect(() => {
    fetch("http://localhost:3000/api/convocatorias") // URL de tu backend
        .then((res) => res.json())
        .then((data) => setConvocatorias(data))
        .catch((err) => console.error("Error cargando convocatorias:", err));
    }, []);

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Listado de Convocatorias</h2>
            <table className="border-collapse border border-gray-400 w-full">
                <thead>
                <tr className="bg-gray-200">
                    <th className="border border-gray-400 p-2">ID</th>
                    <th className="border border-gray-400 p-2">Nombre</th>
                    <th className="border border-gray-400 p-2">Tipo</th>
                    <th className="border border-gray-400 p-2">Beneficiarios</th>
                    <th className="border border-gray-400 p-2">Fecha Inicio</th>
                    <th className="border border-gray-400 p-2">Fecha Final</th>
                    <th className="border border-gray-400 p-2">Documento</th>
                </tr>
                </thead>
            <tbody>
        {convocatorias.map((c) => (
            <tr key={c.idConvocatoria}>
                <td className="border border-gray-400 p-2">{c.idConvocatoria}</td>
                <td className="border border-gray-400 p-2">{c.conNombre}</td>
                <td className="border border-gray-400 p-2">{c.conTipo}</td>
                <td className="border border-gray-400 p-2">{c.conCantidadBeneficiarios}</td>
                <td className="border border-gray-400 p-2">{c.conFechaInicio}</td>
                <td className="border border-gray-400 p-2">{c.conFechaFinal}</td>
                <td className="border border-gray-400 p-2">
                    <a
                    href={`/documentos/${c.conDocumento}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 underline"
                    >
                    {c.conDocumento}
                </a>
                </td>
            </tr>
        ))}
        </tbody>
        </table>
    </div>
    );
}

export default ListarConvocatorias;
