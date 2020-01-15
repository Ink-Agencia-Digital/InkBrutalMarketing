<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Objetivos y desafíos</h1>
        <br />
        <div class="form-group">
          <h3>Persona</h3>
          <select id="persona" class="form-control">
            <option selected>Persona</option>
          </select>
        </div>
        <br />
        <table class="table">
          <thead>
            <tr>
              <th scope="col">
                #
              </th>
              <th scope="col">
                Pregunta
              </th>
              <th scope="col">
                Respuesta
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>
                <label class="" for="pregunta1">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="otro"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>
                <label class="" for="pregunta2">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="respuesta"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>
                <label class="" for="pregunta3">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="respuesta"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td>
                <label class="" for="pregunta4">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="respuesta"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td>
                <label class="" for="pregunta5">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="respuesta"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">6</th>
              <td>
                <label class="" for="pregunta6">Pregunta</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="respuesta"
                  placeholder="Respuesta"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <br />
        <button
          type="submit"
          class="btn btn-dark"
          style="background-color: #344675;"
        >
          Guardar
        </button>
      </form>
    </div>
  </div>
</template>
