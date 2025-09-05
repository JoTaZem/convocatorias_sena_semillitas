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
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md">
        <h2 className="text-2xl font-bold text-gray-800 text-center mb-6">
          Agregar Usuario <span className="text-blue-600">(Evaluador)</span>
        </h2>
        
        <form onSubmit={handleSubmit} className="space-y-5">
          {}
          <div>
            <label className="block text-gray-700 font-medium mb-1">
              Nombre:
            </label>
            <input
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              type="text"
              placeholder="Escribe el nombre"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          {/* Campo Email */}
          <div>
            <label className="block text-gray-700 font-medium mb-1">
              Email:
            </label>
            <input
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              type="email"
              placeholder="ejemplo@correo.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          {/* Botón */}
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
          >
            Agregar Usuario
          </button>
        </form>
      </div>
    </div>
  );
}

export default AgregarUsuario;
