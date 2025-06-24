$fn = 50;


difference() {
	union() {
		cylinder(h = 9, r = 7.0000000000);
	}
	union() {
		cylinder(h = 9, r = 3.2500000000);
		cylinder(h = 9, r = 1.8000000000);
		cylinder(h = 9, r = 1.8000000000);
		cylinder(h = 9, r = 1.8000000000);
	}
}