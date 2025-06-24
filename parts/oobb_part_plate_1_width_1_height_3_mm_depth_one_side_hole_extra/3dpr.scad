$fn = 50;


difference() {
	union() {
		cylinder(h = 3, r = 7.0000000000);
	}
	union() {
		cylinder(h = 3, r = 3.2500000000);
		cylinder(h = 3, r = 1.8000000000);
		cylinder(h = 3, r = 1.8000000000);
		cylinder(h = 3, r = 1.8000000000);
	}
}