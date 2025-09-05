import useListarConvocatorias from "../../hooks/useListarModelo";

const listarConvocatorias = () =>{

    const convocatorias = useListarConvocatorias()
    return(
        <>
            <div className="w-50" style={{margin: '0 auto'}}>
            <h2 className="text-center">LISTA DE CONVOCATORIAS</h2>
            <table className="table table-bordered">
                <thead className="table-dark">
                    <tr>
                        <th>Nombre</th>
                        <th>Tipo</th>
                        <th># beneficiarios </th>
                        <th>Fecha cierre</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        convocatorias.map(convocatoria=>(
                            <tr>
                                <td>{convocatoria.conNombre}</td>
                                <td>convocatoria.conTipo.tipNombre</td>
                                <td>convocatoria.conCatidadBeneficiarios</td>
                                <td>convocatoria.conFechaFinal</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
            </div>
        </>
    )
}

export default listarConvocatorias