<template>
  <div class="container">
    <div class="col-md-8">
      <form @submit.prevent="onSubmit">
        <br /><br />
        <h1>Empresa</h1>
        <br />
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="empresa">Empresa</label>
            <input
              type="text"
              class="form-control"
              v-model="EMP_Nombre_Empresa"
              placeholder="Nombre Empresa"
            />
          </div>
          <div class="form-group col-md-6">
            <label for="tipo">Tipo empresa</label>
            <select id="tipo" class="form-control">
              <option selected>Tipo empresa</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-8">
            <label for="proyecto">Nombre del proyecto</label>
            <input type="text" class="form-control" id="proyecto" />
          </div>
        </div>
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

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      error: null
    };
  },
  methods: {
    onSubmit() {
      if(!this.EMP_Nombre_Empresa) {
        this.error = "Por favor digite un nombre de empresa";
      } else if (this.EMP_Nombre_Empresa.length > 100) {
        this.error = "El nombre de la empresa no puede ser superior a 100 caracteres";
      } else {
        let endpoint = "/api/empresa/";
        let method = "POST";
        apiService(endpoint, method, { EMP_Nombre_Empresa: this.EMP_Nombre_Empresa })
          .then(() => {
          this.$router.push({
            name: "principal_empresa"
          });
        });
      }
    }
  }
};
</script>

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
