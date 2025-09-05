import {Routes, Route } from 'react-router-dom'
import ListConvocatorias from '../pages/lider/ListConvocatorias.jsx'

const  AppRouter=()=> {
  return (       
        <Routes>
          <Route path="/" element={<ListConvocatorias />} />             
        </Routes>   
  );
}

export default AppRouter