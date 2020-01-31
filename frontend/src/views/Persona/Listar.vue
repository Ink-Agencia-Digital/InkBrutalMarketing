<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Personas</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link :to="{ name: 'crear_persona' }" class="btn btn-info">
                <i class="material-icons" style="color:white;">add</i>Crear
              </router-link>
            </li>
          </ul>
        </div>
        <div class=" body table-responsive">
          <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
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
              <tr v-for="(psn, index) in personas" :key="psn.PSN_Id_Persona">
                <th scope="row">
                  {{ ++index }}
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
                      name: 'listar_comportamiento',
                      params: { id: psn.PSN_Id_Persona }
                    }"
                    :title="'Comportamientos'"
                  >
                    <i
                      class="material-icons text-info"
                      style="font-size: 20px;"
                    >
                      extension
                    </i>
                  </router-link>
                  <router-link
                    :to="{
                      name: 'listar_objetivo',
                      params: { id: psn.PSN_Id_Persona }
                    }"
                    :title="'Objetivos'"
                  >
                    <i
                      class="material-icons text-info"
                      style="font-size: 20px;"
                    >
                      event
                    </i>
                  </router-link>
                  <router-link
                    :to="{
                      name: 'editar_persona',
                      params: { id: psn.PSN_Id_Persona }
                    }"
                    title="Editar este Registro"
                  >
                    <i
                      class="material-icons text-info"
                      style="font-size: 20px;"
                    >
                      edit
                    </i>
                  </router-link>
                  <button
                    type="button"
                    class="btn-accion-tabla"
                    title="Eliminar este Registro"
                    @click="deletePersona(psn.PSN_Id_Persona)"
                  >
                    <i
                      class="material-icons text-danger"
                      style="font-size: 20px;"
                    >
                      delete
                    </i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
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
    </div>
  </section>
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
