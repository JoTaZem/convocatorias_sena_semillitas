import {Routes, Route } from 'react-router-dom'
import ListConvocatorias from '../pages/lider/ListConvocatorias.jsx'
import listarConvocatorias from '../pages/lider/ListarConvocatorias.jsx';

const  AppRouter=()=> {
  return (       
        <Routes>
          <Route path="/" element={listarConvocatorias}/>             
          <Route path="/aprendices" element={listarAprendices}/>             
        </Routes>   
  );
}

export default AppRouter