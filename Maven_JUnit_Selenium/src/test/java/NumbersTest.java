import org.checkerframework.common.value.qual.StaticallyExecutable;
import org.junit.Before;
import org.junit.Test;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public class NumbersTest {
    public Numbers n;

    @Before
    public void start(){
        n = new Numbers();
    }

    @Test
    public void addTest() {
        assertEquals(n.add(10, 12), 22);
    }

    @Test
    public void testDiv() {
        assertEquals(n.div(1000, 25), 40);
    }

    @Test (expected = ArithmeticException.class)
    public void testDivByNull() {
        assertEquals(n.div(10, 0), 10);
    }

    @Test
    public void testFactorial() {
        long[] res = new long[] {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800};
        for (int i = 0; i<12; i++){
            assertEquals(n.factorial(i), res[i]);
        }
    }
}