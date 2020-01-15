<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Proceso de Compra</h1>
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
                Etapa
              </th>
              <th scope="col">
                Idea
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">
                1
              </th>
              <td>
                <label class="" for="etapa1">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">
                2
              </th>
              <td>
                <label class="" for="etapa2">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">
                3
              </th>
              <td>
                <label class="" for="etapa3">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">
                4
              </th>
              <td>
                <label class="" for="etapa4">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">
                5
              </th>
              <td>
                <label class="" for="etapa5">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
                />
              </td>
            </tr>
            <tr>
              <th scope="row">
                6
              </th>
              <td>
                <label class="" for="etapa6">Etapa</label>
              </td>
              <td>
                <input
                  type="text"
                  class="form-control"
                  id="idea"
                  placeholder="Idea"
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
