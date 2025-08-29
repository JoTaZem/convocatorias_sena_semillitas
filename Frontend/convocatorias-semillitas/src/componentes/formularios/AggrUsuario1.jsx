import React, { useState } from "react";

function AgregarUsuario() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name || !email) {
      alert('Por favor complete todos los campos.');
      return;
    }
    console.log('Usuario agregado:', { name, email, tipo: 'evaluador' });
    alert('Usuario agregado correctamente');
    setName('');
    setEmail('');
  };

  return (
    <div>
      <h2>Agregar Usuario (Tipo Evaluador)</h2>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input 
        className="txtName"
          type="text" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
        />

        <label>Email:</label>
        <input
        className="txtEmail" 
          type="email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />

        <button type="submit">Agregar Usuario</button>
      </form>
    </div>
  );
}

export default AgregarUsuario;
