package contest


class Aresta(
        val verticeFinal: Verticie,
        val peso: Int
) {
    override fun toString(): String {
        return "v${verticeFinal.id}($peso)"
    }
}


class Verticie(val id: Int) {
    val arestas = mutableListOf<Aresta>()

    fun addAresta(vertice: Verticie,  peso: Int) {
        val aresta = Aresta(vertice, peso)
        arestas.add(aresta)
    }

    override fun toString(): String {
        val strings = mutableListOf("v$id ->")

        for (aresta in arestas)
            strings.add(aresta.toString())

        return strings.joinToString(separator = " ", postfix = "\n")
    }
}


class Grafo() {
    var next: Grafo? = null
    var qntAresta = 0
    private set

    val vertices = mutableMapOf<Int, Verticie>()

    fun addUnilateral(origem: Int, destino: Int, peso: Int) {
        add(origem, destino, peso, bilateral = false)
    }

    fun addBilateral(ponto1: Int, ponto2: Int, peso: Int) {
        add(ponto1, ponto2, peso, bilateral = true)
    }

    private fun add(value1: Int, value2: Int, peso: Int, bilateral: Boolean = false) {
        val vertice1 =  vertices[value1] ?: Verticie(value1)
        val vertice2 =  vertices[value2] ?: Verticie(value2)

        vertice1.addAresta(vertice2, peso)
        if (bilateral)
            vertice2.addAresta(vertice1, peso)

        vertices[value1] = vertice1
        vertices[value2] = vertice2

        qntAresta += if (bilateral) 2 else 1
    }

    override fun toString(): String {
        var string = "Quantiade de vertices ${vertices.size}\n"
        string += "Quantiade de arestas $qntAresta\n\n"

        val items = vertices.values.sortedBy { it.id }

        for (verticie in items)
            string += verticie.toString()
        return string
    }
}


fun main(args: Array<String>) {
    val grafo = Grafo()

    grafo.addUnilateral(0, 1, 2)
    grafo.addUnilateral(1, 2, 4)
    grafo.addUnilateral(2, 0, 12)
    grafo.addUnilateral(2, 4, 40)
    grafo.addUnilateral(3, 1, 3)
    grafo.addUnilateral(4, 3, 8)

    grafo.addBilateral(5, 6, 60)
    println(grafo)
}
