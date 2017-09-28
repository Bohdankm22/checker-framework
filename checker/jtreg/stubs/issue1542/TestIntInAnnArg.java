/*
 * @test
 * @summary Testing long values in @IntRange
 * https://github.com/typetools/checker-framework/issues/1542
 * @compile -XDrawDiagnostics -processor org.checkerframework.common.value.ValueChecker -Astubs=intdeclaration.astub TestIntInAnnArg.java -AstubWarnIfNotFound
 */
package issue1542;

import org.checkerframework.common.value.qual.IntRange;

class Main {
    static int range(boolean big) {
        if (big) {
            return 20000;
        } else {
            return 3;
        }
    }
}

class Call {
    void do_things() {
        @IntRange(from = 3, to = 20000) int x = Main.range(true);
    }
}
