import useListarConvocatorias from "../../hooks/useListarConvocatorias"

const ListConvocatorias = () =>{
    const {listaConvocatorias, cargando} = useListarConvocatorias()
    if (cargando) return <p>Cargando convocatorias</p>
    
    return (
        <>
            <table className="table table-bordered">
                <thead className="table-secondary">
                    <tr className="text-center">
                        <th>Nombre</th>
                        <th>Tipo Convocatoria</th>
                        <th>Cantidad Beneficiarios</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        listaConvocatorias.map((convocatoria)=>(
                            <tr>
                                <td>{convocatoria.conNombre}</td>
                                <td>{convocatoria.conTipo.tipNombre}</td>
                                <td>{convocatoria.conCantidasBeneficiarios}</td>
                            </tr>

                        ))
                    }
                </tbody>
            </table>
        </>
    )
}
export default ListConvocatorias
