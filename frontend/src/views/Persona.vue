<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Persona</h1>
        <br />
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="nombre">Nombre</label>
            <input type="text" class="form-control" id="nombre" />
          </div>
          <div class="form-group col-md-6">
            <label for="apellido">Apellido</label>
            <input type="text" class="form-control" id="apellido" />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="edad">Edad</label>
            <input type="number" class="form-control" id="edad" />
          </div>
          <div class="form-group col-md-6">
            <label for="sexo">Sexo</label>
            <select id="sexo" class="form-control">
              <option selected>Elige uno</option>
              <option>Femenino</option>
              <option>Masculino</option>
              <option>Otro</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="escolaridad">Escolaridad</label>
            <input type="text" class="form-control" id="escolaridad" />
          </div>
          <div class="form-group col-md-6">
            <label for="cargo">Cargo</label>
            <input type="text" class="form-control" id="cargo" />
          </div>
        </div>
        <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
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

<style>
.dang {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
