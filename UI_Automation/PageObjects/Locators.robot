*** Variables ***
${URL}    https://www.saucedemo.com/

${TXT_USER_NAME}    id:user-name
${TXT_PASSWORD}     id:password
${LOGIN_BTN}    xpath://input[@type="submit"]

${CLICK_BOLT_T_SHIRT}       id:add-to-cart-sauce-labs-bolt-t-shirt
${CLICK_FLEECE_JACKET}      id:add-to-cart-sauce-labs-fleece-jacket
${CLICK_CART_ICON}        id:shopping_cart_container


${CLICK_CHEKOUT}        id:checkout

${ENTER_FIRSTNAME}      id:first-name
${ENTER_LASTNAME}      id:last-name
${ENTER_POSTAL_CODE}      id:postal-code
${CONTINUE}     id:continue

#price locators
${PRICE_BOLT}        xpath:(//div[@data-test="inventory-item-price"])[1]
${PRICE_JACKET}      xpath:(//div[@data-test="inventory-item-price"])[2]

${ITEM_TOTAL}        xpath://div[@class='summary_subtotal_label']
${TOTAL_WITH_TAX}    xpath://div[@class='summary_total_label']

# Finish
${FINISH}       id:finish

# Success msg
${SUCCESS_MESSAGE}    xpath://h2[@class='complete-header']