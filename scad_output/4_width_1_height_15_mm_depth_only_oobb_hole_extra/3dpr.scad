$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-24.5000000000, 2.0000000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [24.5000000000, 2.0000000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [-24.5000000000, -2.0000000000, 0]) {
				cylinder(h = 15, r = 5);
			}
			translate(v = [24.5000000000, -2.0000000000, 0]) {
				cylinder(h = 15, r = 5);
			}
		}
	}
	union() {
		translate(v = [-22.5000000000, 0.0000000000, 0]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [-7.5000000000, 0.0000000000, 0]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [7.5000000000, 0.0000000000, 0]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
		translate(v = [22.5000000000, 0.0000000000, 0]) {
			translate(v = [0, 0, -100]) {
				cylinder(h = 200, r = 3.2500000000);
			}
		}
	}
}