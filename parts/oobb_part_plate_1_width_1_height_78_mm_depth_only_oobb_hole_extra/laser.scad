$fn = 50;


difference() {
	union() {
		cylinder(h = 78, r = 7.0000000000);
	}
	union() {
		translate(v = [0, 0, -100]) {
			cylinder(h = 200, r = 3.0000000000);
		}
	}
}