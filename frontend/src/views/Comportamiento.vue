<template>
  <div class="container">
    <div class="col-md-8">
      <form>
        <br /><br />
        <h1>Comportamiento</h1>
        <br />
        <div class="form-group">
          <h3>Persona</h3>
          <select id="persona" class="form-control">
            <option selected>Persona</option>
          </select>
        </div>
        <br />
        <div class="form-group ">
          <h4>Describe sus hábitos y su día a día</h4>
          <br />
          <h5 for="descripcion">Descripción</h5>
          <textarea class="form-control" aria-label="With textarea"></textarea>
        </div>
        <br /><br />
        <div class="form-group ">
          <h4>¿Cuáles son los medios de comunicación usados por tu Persona?</h4>
          <br />
          <h5 for="medio">Medios</h5>
          <br />
          <div class="custom-control custom-switch">
            <div class="row">
              <div class="col">
                <ul>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio1"
                    />
                    <label class="custom-control-label" for="medio1">
                      Redes sociales
                    </label>
                  </li>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio2"
                    />
                    <label class="custom-control-label" for="medio2">
                      Blog
                    </label>
                  </li>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio3"
                    />
                    <label class="custom-control-label" for="medio3">
                      Anuncios en medios tradicionales
                    </label>
                  </li>
                </ul>
              </div>
              <div class="col">
                <ul>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio4"
                    />
                    <label class="custom-control-label" for="medio4">
                      Anuncios de medios digitales
                    </label>
                  </li>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio5"
                    />
                    <label class="custom-control-label" for="medio5">
                      Email
                    </label>
                  </li>
                  <li>
                    <input
                      type="checkbox"
                      class="custom-control-input"
                      id="medio6"
                    />
                    <label class="custom-control-label" for="medio6">
                      Télefono
                    </label>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="form-group">
            <label for="otro">Otros</label>
            <input
              type="text"
              class="form-control"
              id="otro"
              placeholder="¿Cúal otro medio?"
            />
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
