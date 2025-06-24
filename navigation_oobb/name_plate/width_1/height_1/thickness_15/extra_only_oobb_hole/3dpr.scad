$fn = 50;


difference() {
	union() {
		cylinder(h = 15, r = 7.0000000000);
	}
	union() {
		translate(v = [0, 0, -100]) {
			cylinder(h = 200, r = 3.2500000000);
		}
	}
}