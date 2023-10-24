describe('Home page test', () => {
  it('Home page elements exist', () => {
    cy.visit('http://localhost:3000/')

    //title exists
    cy.get('.v-toolbar-title__placeholder > .v-btn > .v-btn__content')

    //main
    cy.get('.v-main')

    //picture present
    cy.get('.centered')

    //register button is present
    cy.get('.v-main > .v-btn')

    //toolbar is present
    cy.get('.v-toolbar__content')

    //login is present
    cy.get('[href="/login"]')

  })

})


