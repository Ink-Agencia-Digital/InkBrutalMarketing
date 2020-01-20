<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Proyecto</h1>
        <br />
        <div class="form-row">
          <div class="form-group col-md-10">
            <label for="proyecto">Nombre del proyecto</label>
            <input type="text" class="form-control" id="proyecto" />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-10">
            <label for="empresa">Empresa</label>
            <select id="empresa" class="form-control">
              <option selected>Empresa</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-10">
            <label for="persona">Persona</label>
            <select id="persona" class="form-control">
              <option selected>Persona</option>
            </select>
          </div>
        </div>
        <br />
        <button
          type="submit"
          class="btn btn-dark"
          style="background-color: #344675;"
        >
          Guardar
        </button>
        <br /><br /><br />
      </form>
    </div>
  </div>
</template>
