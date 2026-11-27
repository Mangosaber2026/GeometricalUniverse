import kotlinx.browser.document
import org.w3c.dom.HTMLElement
import org.w3c.dom.HTMLInputElement

fun main() {
    initializeProjectSearch()
}

private fun initializeProjectSearch() {

    val searchInput = document.getElementById(
        "project-search-input"
    ) as? HTMLInputElement ?: return

    val projectCards = document.getElementsByClassName(
        "project-card"
    )

    searchInput.addEventListener("input") { _ ->

        val query = searchInput.value
            .trim()
            .lowercase()

        for (index in 0 until projectCards.length) {

            val card = projectCards.item(index)
                as? HTMLElement ?: continue

            val cardText = card.textContent
                ?.lowercase()
                .orEmpty()

            card.hidden = query.isNotEmpty() &&
                !cardText.contains(query)
        }
    }

    searchInput.disabled = false
}