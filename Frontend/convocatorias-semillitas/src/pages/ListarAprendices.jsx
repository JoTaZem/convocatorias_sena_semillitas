import useListarModelo from "../../hooks/useListarModelo";

const listarAprendices = () =>{

    const convocatorias = useListarConvocatorias()
    return(
        <>
            <div className="w-50" style={{margin: '0 auto'}}>
            <h2 className="text-center">LISTA DE APRENDICES</h2>
            <table className="table table-bordered">
                <thead className="table-dark">
                    <tr>
                        <th>Nombre</th>
                        <th>correo</th>
                        
                    </tr>
                </thead>
                <tbody>
                    {
                        convocatorias.map(aprendiz=>(
                            <tr>
                                <td>{aprendiz.aprUsuario.first_name}</td>
                                <td>aprendiz.aprUsuario.email</td>
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