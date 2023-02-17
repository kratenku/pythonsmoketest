Feature: Ingresar a pagina de compra
  Scenario: Diligenciar fórmulario de registro
    Given navigator edge
    When seleccione botón de ingreso
    And ingresar nombre
    And ingresar apellido
    And ingresar correo