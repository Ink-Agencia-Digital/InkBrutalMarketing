<template>
  <div class="container">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Persona</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link :to="{ name: 'crear_persona' }" class="btn btn-info">
                Crear
              </router-link>
            </li>
          </ul>
        </div>
        <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
        <div class=" body table-responsive">
          <table class="table">
            <thead class="thead-dark">
              <tr>
                <th scope="col">
                  #
                </th>
                <th scope="col">
                  Nombre
                </th>
                <th scope="col">
                  Apellido
                </th>
                <th scope="col">
                  Escolaridad
                </th>
                <th scope="col">
                  Acción
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="psn in personas" :key="psn.PSN_Id_Persona">
                <th scope="row">
                  {{ psn.PSN_Id_Persona }}
                </th>
                <td>
                  <label class="" for="nombre">
                    {{ psn.PSN_Nombres_Persona }}
                  </label>
                </td>
                <td>
                  <label class="" for="apellido">
                    {{ psn.PSN_Apellidos_Persona }}
                  </label>
                </td>
                <td>
                  <label class="" for="escolaridad">
                    {{ psn.PSN_Escoladidad_Persona.ESC_Nombre_Escolaridad }}
                  </label>
                </td>
                <td>
                  <router-link
                    :to="{
                      name: 'editar_persona',
                      params: { id: psn.PSN_Id_Persona }
                    }"
                    class="bp btn-primary"
                  >
                    Modificar
                  </router-link>
                  <button
                    type="button"
                    class="bpn btn-danger"
                    @click="deletePersona(psn.PSN_Id_Persona)"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="my-4">
        <p v-show="loadingPersonas">...Cargando...</p>
        <button
          v-show="nextPersona"
          @click="getPersonas('MAS')"
          class="btn btn-sm btn-outline-success"
        >
          Cargar Más
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      personas: [],
      loadingPersonas: false,
      nextPersona: null
    };
  },
  methods: {
    getPersonas(accion = null) {
      let endpoint = "/api/persona-join/";
      if (accion == "DELETE") {
        this.personas = [];
        apiService(endpoint).then(data => {
          this.personas.push(...data.results);
        });
      } else {
        if (this.nextPersona) {
          endpoint = this.nextPersona;
        }
        this.loadingPersonas = true;
        apiService(endpoint).then(data => {
          this.personas.push(...data.results);
          this.loadingPersonas = false;
          if (data.next) {
            this.nextPersona = data.next;
          } else {
            this.nextPersona = null;
          }
        });
      }
    },
    async deletePersona(persona) {
      let endpoint = `/api/persona/${persona}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getPersonas("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    }
  },
  created() {
    this.getPersonas();
  }
};
</script>

<style>
.b {
  padding: 6px 12px;
  text-align: center;
  font-size: 16px;
  border-radius: 8px;
}
.bp {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
.bpn {
  padding: 2% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
