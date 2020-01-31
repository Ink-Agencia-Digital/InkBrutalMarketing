<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Medios</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link :to="{ name: 'crear_medio' }" class="btn btn-info">
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
                <th scope="col">#</th>
                <th scope="col">Nombre del Medio</th>
                <th scope="col">Descripcion</th>
                <th scope="col">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(mdo, index) in medios" :key="mdo.MDO_Id_Medio">
                <th scope="row">
                  {{ ++index }}
                </th>
                <td>
                  <label class="">
                    <i class="fa " v-bind:class="mdo.MDO_Icono_Medio"></i>
                    {{ mdo.MDO_Nombre_Medio }}
                  </label>
                </td>
                <td>
                  <label class="">
                    {{ mdo.MDO_Descripcion_Medio }}
                  </label>
                </td>
                <td>
                  <router-link
                    :to="{
                      name: 'editar_medio',
                      params: { id: mdo.MDO_Id_Medio }
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
                    @click="deleteMedio(mdo.MDO_Id_Medio)"
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
            <p v-show="loadingMedios">...Cargando...</p>
            <button
              v-show="nextMedio"
              @click="getMedios('MAS')"
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
      medios: [],
      nextMedio: null,
      loadingMedios: false
    };
  },
  methods: {
    getMedios(accion = null) {
      let endpoint = "/api/medio/";
      if (accion == "DELETE") {
        this.medios = [];
        apiService(endpoint).then(data => {
          this.medios.push(...data.results);
        });
      } else {
        if (this.nextMedio) {
          endpoint = this.nextMedio;
        }
        this.loadingMedios = true;
        apiService(endpoint).then(data => {
          this.medios.push(...data.results);
          this.loadingMedios = false;
          if (data.next) {
            this.nextMedio = data.next;
          } else {
            this.nextMedio = null;
          }
        });
      }
    },
    async deleteMedio(medio) {
      let endpoint = `/api/medio/${medio}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getMedios("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    }
  },
  created() {
    this.getMedios();
  }
};
</script>

<style>
.b {
  padding: 2% 3%;
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
