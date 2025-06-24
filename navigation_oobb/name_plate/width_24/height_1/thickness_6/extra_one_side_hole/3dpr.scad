$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-174.5000000000, 2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [174.5000000000, 2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [-174.5000000000, -2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [174.5000000000, -2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
		}
	}
	union() {
		translate(v = [-172.5000000000, 0.0000000000, 0]) {
			cylinder(h = 6, r = 3.2500000000);
		}
		translate(v = [-172.5000000000, 0.0000000000, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		translate(v = [-172.5000000000, 0.0000000000, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		translate(v = [-172.5000000000, 0.0000000000, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
	}
}