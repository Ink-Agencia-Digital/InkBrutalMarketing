<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Medio</h1>
        <br />
        <div class="form-group">
          <h5>Nombre del Medio</h5>
          <input type="text" class="form-control" id="medio" />
        </div>
        <br />
        <div class="form-group ">
          <h5 for="descripcion">Descripción</h5>
          <textarea class="form-control" aria-label="With textarea"></textarea>
        </div>
        <br /><br />
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
.background {
  position: absolute;
  z-index: 1;
  width: 98%;
  height: 169%;
  padding-top: 0%;
  padding-left: 0%;
  padding-right: 0%;
}
</style>
