import { useState, useEffect, useCallback } from "react"
const API_URL = "http://localhost:8000/api/convocatoria/"

const useListarConvocatorias= ()=> {
    const [listaConvocatorias, setLista] = useState([])
    const [cargando, setCargando] = useState(true)

    const obtenerConvocatorias = useCallback(() => {
    fetch(`${API_URL}`)
      .then(res=>res.json())
      .then((data) => {
        console.log(data)
        setLista(data)
        setCargando(false)
      })
      .catch((error) => {
        console.error(error)
        setCargando(false)
      });
    }, []);
    
    useEffect(() => {
        obtenerConvocatorias()
    }, [])
    
    return { listaConvocatorias, cargando };
}
export default useListarConvocatorias;

