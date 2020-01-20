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
              maxlength="100"
            />
          </div>
          <div class="form-group col-md-6">
            <label for="tipo">Tipo empresa</label>
            <select id="tipo" class="form-control">
              <option selected>Tipo empresa</option>
            </select>
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
  props: {
    id: {
      type: Number,
      required: true
    },
    nombreAnterior: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      EMP_Nombre_Empresa: this.nombreAnterior,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.EMP_Nombre_Empresa) {
        this.error = "Por favor digite un nombre de empresa";
      } else if (this.EMP_Nombre_Empresa.length > 100) {
        this.error =
          "El nombre de la empresa no puede ser superior a 100 caracteres";
      } else {
        let endpoint = `/api/empresa/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, {
          EMP_Nombre_Empresa: this.EMP_Nombre_Empresa
        }).then(() => {
          this.$router.push({
            name: "listar_empresa"
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/empresa/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.nombreAnterior = data.EMP_Nombre_Empresa;
    return next();
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
