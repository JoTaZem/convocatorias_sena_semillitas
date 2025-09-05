import { useState, useEffect, useCallback } from "react"
const API_URL = "http://localhost:8000/api/convocatoria/"

const useListarModelo= ()=> {
    const [listaConvocatorias, setLista] = useState([])
    const [cargando, setCargando] = useState(true)

    const obtenerConvocatorias = useCallback(() => {
    fetch(`${URL_API}${valor}/`)
      .then(res=>res.json())
      .then(datos => {
        
        setLista(datos)
        
      })
      .catch(error => {
        console.log(error)
        
      });
    }, []);
    
    useEffect(() => {
        obtenerLista()
    }, [obtenerLista])
    
    return lista;
}
export default useListarModelo;

