import AgregarUsuario from "./componentes/formularios/AggrUsuario1";
import ListarBeneficiarios from "./componentes/ListarBeneficiarios5";
import ListarPostulados from "./componentes/ListarPostulados4";
//import RegistrarConvocatorias from './componentes/formularios/RegistrarConvocatorias';

function App() {
  return (
    <div className="App">
      <h1>Gestión de Convocatorias</h1>
      <AgregarUsuario />
      <ListarPostulados/>
      <ListarBeneficiarios/>


    </div>
  );
}

export default App;
