import AppRouter from "./routes/appRoutes.jsx";
//import AgregarUsuario from "./componentes/formularios/AggrUsuario1";
//import ListarBeneficiarios from "./componentes/ListarBeneficiarios5";
//import ListarPostulados from "./componentes/ListarPostulados4";
import Home from "./pages/Home.jsx";
import PiePagina from "./pages/PiePagina.jsx";
//import Encabezado from "./pages/Encabezado.jsx";

//import RegistrarConvocatorias from './componentes/formularios/RegistrarConvocatorias';

const App = ()=>{
  return (
    <>
    <div className="App">
      <h1>Gestión de Convocatorias</h1>
      <Home/>
      <PiePagina />
      <AppRouter/>

    </div>
    </>
  );
}

export default App;
