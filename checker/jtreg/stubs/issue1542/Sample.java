/*
 * @test
 * @summary Testing long values in @IntRange
 * @compile -XDrawDiagnostics -processor org.checkerframework.common.value.ValueChecker -Astubs=intdeclaration.astub Sample.java
 */

import org.checkerframework.common.value.qual.IntRange;

public class Sample {
    static int range(boolean big) {
        return 1;
    }
}

class UseIntRange {
    void do_things() {
        @IntRange(from = 3, to = 20000) int x = Sample.range(true);
    }
}
