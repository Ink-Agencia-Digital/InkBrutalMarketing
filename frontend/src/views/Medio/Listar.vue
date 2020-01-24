<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Medio</h1>
      <br />
      <router-link :to="{ name: 'crear_medio' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
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
          <tr v-for="mdo in medios" :key="mdo.MDO_Id_Medio">
            <th scope="row">
              {{ mdo.MDO_Id_Medio }}
            </th>
            <td>
              <label class="">
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
                :to="{ name: 'editar_medio', params: { id: mdo.MDO_Id_Medio } }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button
                type="button"
                class="bpn btn-danger"
                @click="deleteMedio(mdo.MDO_Id_Medio)"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
    </div>
  </div>
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
